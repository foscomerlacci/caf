(function($) {
    $(function() {
        var
            selectField = $('#id_stato'),
            verified = $('.form-row.field-congiunto');
            c_da_resettare = $('#id_congiunto');

        function toggleVerified(value) {
             if (value === 'sin') {
                verified.hide();
                 c_da_resettare.val(' ');

             } else {
                 verified.show();
             }
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());

        }
        );
    });
})(django.jQuery);


