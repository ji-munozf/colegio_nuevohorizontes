$(document).ready(function () {
    const regionSelect = $('#region-select');
    const comunaSelect = $('#comuna-select');

    regionSelect.on('change', function () {
        const regionId = $(this).val();

        if (regionId === '') {
            comunaSelect.empty().append($('<option>').text('Seleccione una comuna').attr('value', ''));
            comunaSelect.prop('disabled', true);
            return;
        }

        axios.get(`/api/comunas/?region=${regionId}`)
            .then(response => {
                const comunas = response.data;

                comunaSelect.empty().append($('<option>').text('Seleccione una comuna').attr('value', ''));
                $.each(comunas, function (index, comuna) {
                    comunaSelect.append($('<option>').text(comuna.nombre_comuna).attr('value', comuna.id_comuna));
                });

                comunaSelect.prop('disabled', comunas.length === 0);
            })
            .catch(error => {
                console.error(error);
            });
    });

    $('input[type="reset"]').click(function () {
        comunaSelect.prop('disabled', true);
    });

    comunaSelect.prop('disabled', true);
});