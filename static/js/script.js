// Get the mobile nav toggle and navmenu elements
const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
const body = document.querySelector('body');

// Add an event listener to the toggle
mobileNavToggle.addEventListener('click', () => {
    body.classList.toggle('mobile-nav-active');
});

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        document.querySelector('.navbar').classList.add('scrolled');
    } else {
        document.querySelector('.navbar').classList.remove('scrolled');
    }
})

document.addEventListener('DOMContentLoaded', function() {
    const heroSection = document.getElementById('hero');
    heroSection.classList.add('loaded');
});

document.addEventListener('DOMContentLoaded', function() {
    const projectList = document.getElementById('project-list');
    const showAllButtonContainer = document.getElementById('show-all-button-container');
    const showAllButton = document.getElementById('show-all-projects');

    try {
        const projectsData = JSON.parse('{{ projects|tojson|safe }}');

        if (showAllButton) {
            showAllButton.addEventListener('click', () => { // Use arrow function
                projectList.innerHTML = ''; // Clear existing projects
                showAllButtonContainer.remove();

                projectsData.forEach(project => {
                    const projectItem = document.createElement('div');
                    projectItem.classList.add('col-md-4', 'project-item');

                    // Use a template literal to build the card HTML
                    projectItem.innerHTML = `
                        <div class="project-card">
                            <div class="project-image">
                                <img src="/static/img/project-placeholder.jpg" alt="${project.title}" class="img-fluid">
                                <div class="project-overlay">
                                    <div class="overlay-content">
                                        <h3>${project.title}</h3>
                                        <p>${project.short_description ? project.short_description : project.description.substring(0, 100) + "..."}</p>
                                        <a href="#" class="btn btn-primary">Learn More</a>
                                    </div>
                                </div>
                            </div>
                            <div class="card-body">
                                <h5 class="card-title">${project.title}</h5>
                                <p class="card-text">${project.description}</p>
                            </div>
                        </div>
                    `;
                    projectList.appendChild(projectItem);
                });
            });
        }
    } catch (error) {
        console.error("Error parsing project data:", error);
        projectList.innerHTML = "<p>Error loading projects.</p>";
    }
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});