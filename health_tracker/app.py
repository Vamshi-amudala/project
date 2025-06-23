from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Vam0410',
    'database': 'health_tracker'
}

app.config['SECRET_KEY'] = 'your_secret_key_here'

def get_db():
    return mysql.connector.connect(**db_config)

@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db()
        cur = conn.cursor()
        
        # Check if username or email already exists
        cur.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
        user = cur.fetchone()
        
        if user:
            flash('Username or email already exists!', 'error')
            return render_template('register.html')
        
        # Hash password and insert user
        password_hash = generate_password_hash(password)
        cur.execute("INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
                   (username, email, password_hash))
        conn.commit()
        cur.close()
        conn.close()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        
        if user and check_password_hash(user[3], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('dashboard'))
        
        flash('Invalid username or password!', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/track', methods=['GET', 'POST'])
def track():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        date = request.form['date']
        weight = request.form['weight']
        steps = request.form['steps']
        sleep_hours = request.form['sleep_hours']
        water_intake = request.form['water_intake']
        mood = request.form['mood']
        notes = request.form['notes']
        
        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO health_records 
                (user_id, date, weight, steps, sleep_hours, water_intake, mood, notes)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                weight = VALUES(weight),
                steps = VALUES(steps),
                sleep_hours = VALUES(sleep_hours),
                water_intake = VALUES(water_intake),
                mood = VALUES(mood),
                notes = VALUES(notes)
            """, (session['user_id'], date, weight, steps, sleep_hours, water_intake, mood, notes))
            conn.commit()
            flash('Health data saved successfully!', 'success')
        except mysql.connector.Error as err:
            flash(f'Error: {err}', 'error')
        finally:
            cur.close()
            conn.close()
        
        return redirect(url_for('dashboard'))
    
    return render_template('track.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT date, weight, steps, sleep_hours, water_intake, mood, notes
        FROM health_records
        WHERE user_id = %s
        ORDER BY date DESC
        LIMIT 7
    """, (session['user_id'],))
    records = cur.fetchall()
    cur.close()
    conn.close()
    
    return render_template('dashboard.html', records=records)

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        username = request.form['username']
        new_password = request.form['new_password']

        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()

        if not user:
            flash('Username not found!', 'error')
            cur.close()
            conn.close()
            return render_template('forgot_password.html')

        password_hash = generate_password_hash(new_password)
        cur.execute("UPDATE users SET password_hash = %s WHERE username = %s", (password_hash, username))
        conn.commit()
        cur.close()
        conn.close()

        flash('Password reset successful! Please login with your new password.', 'success')
        return redirect(url_for('login'))

    return render_template('forgot_password.html')

if __name__ == '__main__':
    app.run(debug=True)