// console.log("Working!!")

document.addEventListener('DOMContentLoaded', function () {
    // const form = document.getElementById('booking-form');
    // const pickupLocation = document.getElementById('id_pickup_location')
    // pickupLocation.addEventListener("onChange", () => console.log("Changed!!"))

    // form.addEventListener('submit', function (event) {
    //     event.preventDefault(); // Prevent the form from submitting

    //     // Retrieve form input values
    //     const pickupLocation = document.getElementById('id_pickup_location').value;
    //     const dropoffLocation = document.getElementById('id_dropoff_location').value;
    //     const vehicleType = document.getElementById('id_vehicle_type').value;
    //     const rateType = document.querySelector('input[name="rate_type"]:checked').value;
    //     const serviceType = document.querySelector('input[name="service_type"]:checked').value;

    //     // Create a JavaScript object to store the values
    //     const bookingData = {
    //         pickup_location: pickupLocation,
    //         dropoff_location: dropoffLocation,
    //         vehicle_type: vehicleType,
    //         rate_type: rateType,
    //         service_type: serviceType,
    //     };

    //     // Log the object for testing (you can do more with it)
    //     console.log("Data", bookingData);

    // Now, you can send this data to your server using AJAX or perform any desired actions.
    // });
    // Get the tracking id of each booking and store in the localstorage
    const tracking_id = document.getElementById("tracking_id")
    console.log(tracking_id.innerHTML)
    const trackingIdValue = tracking_id.innerHTML;
    localStorage.setItem("tracking_id", trackingIdValue);


});
