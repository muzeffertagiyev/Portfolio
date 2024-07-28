(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  // Function to hide the flash message after a specified time (in milliseconds)
    function hideFlashMessage() {
      var flashMessage = document.getElementById("flash-message");
      if (flashMessage) {
          setTimeout(function() {
              flashMessage.style.display = "none";
          }, 5000); // Change 5000 to the desired duration (in milliseconds)
      }
  }
    // Call the function to hide the flash message
    hideFlashMessage();


    // Function to add "active" class to the appropriate link
    function setActiveLink() {
      const currentLocation = window.location.pathname;
      const navLinks = document.querySelectorAll('.nav-link');
  
      navLinks.forEach(link => {
        const linkUrl = link.getAttribute('href');
        if (currentLocation === linkUrl) {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      });
    }
  
    // Call the function to set the active link initially
    setActiveLink();

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('body').classList.toggle('mobile-nav-active')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })
  /**
   * Hero type effect
   */
  const typed = select('.typed')
  if (typed) {
    let typed_strings = typed.getAttribute('data-typed-items')
    typed_strings = typed_strings.split(',').map(str => str.replace(/&/g, '&amp;'))
    new Typed('.typed', {
      strings: typed_strings,
      loop: true,
      typeSpeed: 100,
      backSpeed: 30,
      backDelay: 1000
    });
  }

  /**
   * Skills animation
   */
  let skilsContent = select('.skills-content');
  if (skilsContent) {
    new Waypoint({
      element: skilsContent,
      offset: '80%',
      handler: function(direction) {
        let progress = select('.progress .progress-bar', true);
        progress.forEach((el) => {
          el.style.width = el.getAttribute('aria-valuenow') + '%'
        });
      }
    })
  }

  /**
   * Porfolio isotope and filter
   */
  window.addEventListener('load', () => {
    let portfolioContainer = select('.portfolio-container');
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: '.portfolio-item'
      });

      let portfolioFilters = select('#portfolio-filters li', true);

      on('click', '#portfolio-filters li', function(e) {
        e.preventDefault();
        portfolioFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        portfolioIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        portfolioIsotope.on('arrangeComplete', function() {
          AOS.refresh()
        });
      }, true);
    }

  });

  /**
   * Initiate portfolio lightbox 
   */
  const portfolioLightbox = GLightbox({
    selector: '.portfolio-lightbox'
  });

  /**
   * Portfolio details slider
   */
  new Swiper('.project-details-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

 
  /**
   * Animation on scroll
   */
  window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    })
  });


})()


// for country flag as per country phone number code
document.addEventListener("DOMContentLoaded", function() {
  var input = document.querySelector("#mobile_phone");
  var iti = window.intlTelInput(input, {
    initialCountry: "auto",
    nationalMode: false, // Show full international format as placeholder
    geoIpLookup: function(callback) {
      fetch("https://ipinfo.io?token=f459bc1138db43")
        .then(response => response.json())
        .then(data => {
          callback(data.country);
        });
    },
    utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.13/js/utils.js"
  });

  // Set the initial country code in the input field
  iti.promise.then(function() {
    var countryData = iti.getSelectedCountryData();
    input.value = "+" + countryData.dialCode + " ";
  });

  // Update the input field with the country code when a new country is selected
  input.addEventListener("countrychange", function() {
    var countryData = iti.getSelectedCountryData();
    input.value = "+" + countryData.dialCode + " ";
  });
});

