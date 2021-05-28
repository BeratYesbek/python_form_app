(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.remove('was-validated-user');
        form.classList.remove('was-validated-password');
        form.classList.remove('was-validated');

        if ($('#username').val() == ''){
          form.classList.add('was-validated-user');
          form.classList.add('was-validated');
        }

        if ($('#password').val() == ''){
          form.classList.add('was-validated-password');
          form.classList.add('was-validated');
        }

      }, false);
    });
  }, false);
})();