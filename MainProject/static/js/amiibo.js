$(document).ready(function() {
    /****************************
    *     Amiibo JavaScript     *
    *****************************/

    var amiibo_modal = document.getElementsByClassName("amiibo_modal")[0];

    /* This contains the list of all elements that will be able to open the modal.
    *  I may want to add more ways to delete later on */
    var modalOpeners = document.getElementsByClassName("amiibo_modalOpener");

    // A list of all of the elements that will close the modal (there are only 2 - exit, and go back buttons)
    var modalClosers = document.getElementsByClassName("amiibo_modalCloser");

    // For every element that was designated to open the modal, give them the onclick function to do so.
    var i;
    for (i = 0; i < modalOpeners.length; i++) {
        modalOpeners[i].onclick = function() {
            amiibo_modal.style.display = "block";
        }
    }

    // For every element that was designated to close the modal, give them the onclick function to do so.
    var i;
    for (i = 0; i < modalClosers.length; i++) {
        modalClosers[i].onclick = function() {
            amiibo_modal.style.display = "none";
        }
    }

    // Copied from https://www.w3schools.com/howto/howto_css_modals.asp
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == amiibo_modal) {
            amiibo_modal.style.display = "none";
        }
    }

    // Dynamically change the name in the modal.
    var nameOnDetailsPage = document.getElementById("amiiboNameForModal").innerHTML;
    document.getElementById("dynamicNameForModal").innerHTML = nameOnDetailsPage;

    /****************************
    *   END Amiibo JavaScript   *
    *****************************/
});