document.addEventListener('DOMContentLoaded', function () {
    const editarBtn = document.getElementById('editarBtn');
    const guardarBtn = document.getElementById('guardarBtn');
    const cancelarBtn = document.getElementById('cancelarBtn');
    const inputs = document.querySelectorAll('input:not(#rut)[disabled]');

    let originalValues = {}; // Almacena los valores originales de los campos

    editarBtn.addEventListener('click', function () {
        guardarOriginalValues(); // Guarda los valores originales antes de habilitar los campos
        editarBtn.classList.add('d-none');
        guardarBtn.classList.remove('d-none');
        cancelarBtn.classList.remove('d-none');
        inputs.forEach(function (input) {
            input.removeAttribute('disabled');
        });
    });

    cancelarBtn.addEventListener('click', function () {
        if (hasChanges()) {
            resetFields(); // Restablece los valores originales si hay cambios
        }
        editarBtn.classList.remove('d-none');
        guardarBtn.classList.add('d-none');
        cancelarBtn.classList.add('d-none');
        inputs.forEach(function (input) {
            input.setAttribute('disabled', 'disabled');
        });
    });

    function guardarOriginalValues() {
        inputs.forEach(function (input) {
            originalValues[input.id] = input.value; // Guarda los valores originales de los campos
        });
    }

    function hasChanges() {
        let hasChanges = false;
        inputs.forEach(function (input) {
            if (input.value !== originalValues[input.id]) {
                hasChanges = true; // Verifica si hay cambios en los valores de los campos
            }
        });
        return hasChanges;
    }

    function resetFields() {
        inputs.forEach(function (input) {
            input.value = originalValues[input.id]; // Restablece los valores originales de los campos
        });
    }
});