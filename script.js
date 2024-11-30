// Data for destinations and packages
const destinations = [
    {
        name: "Maldives",
        image: "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
        description: "Crystal-clear waters and luxurious resorts."
    },
    {
        name: "Paris, France",
        image: "https://images.unsplash.com/photo-1502602898657-3e91760cbb34",
        description: "The city of love and iconic landmarks."
    },
    {
        name: "Bali, Indonesia",
        image: "https://www.holidify.com/images/bgImages/BALI.jpg",
        description: "Lush greenery, beaches, and spiritual retreats."
    },
    {
        name: "Santorini, Greece",
        image: "https://images.unsplash.com/photo-1507089947368-19c1da9775ae",
        description: "Stunning sunsets and white-washed architecture."
    },
    {
        name: "Tokyo, Japan",
        image: "https://cdn.shedefined.com.au/wp-content/uploads/2024/02/24151840/Travel-guide-to-Tokyo-Japan-HERO-960x540-1.jpg",
        description: "Modern cityscapes and cultural experiences."
    },
    {
        name: "New York, USA",
        image: "https://cdn.britannica.com/94/167894-050-C7E2C482/Brooklyn-Bridge-East-River-New-York-City.jpg",
        description: "The city that never sleeps."
    }
];

const packages = [
    {
        name: "Luxury Beach Getaway",
        image: "https://images.unsplash.com/photo-1568572933382-74d440642117",
        price: "$2,999",
        details: "5 nights in a private villa with ocean views."
    },
    {
        name: "European Adventure",
        image: "https://images.unsplash.com/photo-1511765224389-37f0e77cf0eb",
        price: "$3,499",
        details: "Visit 5 countries in 10 days with guided tours."
    },
    {
        name: "Mountain Retreat",
        image: "https://images.unsplash.com/photo-1513415564515-763d91423bdd",
        price: "$2,299",
        details: "A week in a cozy mountain lodge with excursions."
    },
    {
        name: "City Explorer",
        image: "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb",
        price: "$1,499",
        details: "4 nights in a top-rated hotel with city tours."
    },
    {
        name: "Cultural Immersion",
        image: "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0",
        price: "$2,499",
        details: "Experience the magic of snow in the most popular winter destinations."
    },    
    {
        name:'Bali Wellness Retreat',
        image: 'https://images.unsplash.com/photo-1537551080512-fb7dd14fbf90',
        price: '$2,999',
        duration: '8 days',
        details: 'Rejuvenating wellness retreat in tropical paradise.'
    }
];


// Function to render destinations
const renderDestinations = () => {
    const destinationsGrid = document.getElementById("destinationsGrid");
    destinations.forEach(destination => {
        const destinationCard = document.createElement("div");
        destinationCard.className = "col-md-4 animate-fade-in";
        destinationCard.innerHTML = `
            <div class="card destination-card">
                <img src="${destination.image || 'https://via.placeholder.com/300x200'}" class="card-img-top" alt="${destination.name}">
                <div class="card-body">
                    <h5 class="card-title">${destination.name}</h5>
                    <p class="card-text">${destination.description}</p>
                </div>
            </div>
        `;
        destinationsGrid.appendChild(destinationCard);
    });
};

// Function to render packages
const renderPackages = () => {
    const packagesGrid = document.getElementById("packagesGrid");
    packages.forEach(packageItem => {
        const packageCard = document.createElement("div");
        packageCard.className = "col-md-4 animate-fade-in";
        packageCard.innerHTML = `
            <div class="card package-card">
                <img src="${packageItem.image || 'https://via.placeholder.com/300x200'}" class="card-img-top" alt="${packageItem.name}">
                <div class="card-body">
                    <h5 class="card-title">${packageItem.name}</h5>
                    <p class="card-text">${packageItem.details}</p>
                    <p class="card-text"><strong>Price:</strong> ${packageItem.price}</p>
                </div>
            </div>
        `;
        packagesGrid.appendChild(packageCard);
    });
};

// Function to populate the dropdown with destinations
const populateDestinationDropdown = () => {
    const destinationDropdown = document.getElementById("destination");
    destinations.forEach(destination => {
        const option = document.createElement("option");
        option.value = destination.name;
        option.textContent = destination.name;
        destinationDropdown.appendChild(option);
    });
};

// Initialize the page
const initializePage = () => {
    renderDestinations();
    renderPackages();
    populateDestinationDropdown();
};

// Call initialize function on page load
document.addEventListener("DOMContentLoaded", initializePage);
