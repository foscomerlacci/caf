(function($) {
    $(function() {
        var selectField = $('#id_prima_casa'),
            // verified = $('.form-row.field-seconda_casa'),
            verified = $('div.form-row:nth-child(8)'),
            sc_da_resettare = $('#id_seconda_casa');

        function toggleVerified(value) {
             if (value === 'False') {

                 verified.hide();
                 sc_da_resettare.prop( "checked", false );

             } else {

                 verified.show();

             }
        }

        // show/hide on load based on previous value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());


        });
    });
})(django.jQuery);

