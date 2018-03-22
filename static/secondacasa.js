(function($) {
    $(function() {
        var prima_casa = $('#id_prima_casa'),
            seconda_casa = $('#id_seconda_casa');

        function toggleseconda_casa(prima_casa) {
            prima_casa == 'False' ? seconda_casa.hide() : seconda_casa.show();
        }

        // show/hide on load based on pervious value of selectField
        toggleseconda_casa(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleseconda_casa($(this).val());
        });
    });
})(django.jQuery);