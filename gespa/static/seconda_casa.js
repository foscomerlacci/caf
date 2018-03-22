(function($) {
    $(function() {
        var selectField = $('#id_prima_casa'),
            verified = $('.form-row.field-seconda_casa');

        function toggleVerified(value) {
             if (value === 'no') {
                verified.hide();
             } else {
                 verified.show();
             }
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);

