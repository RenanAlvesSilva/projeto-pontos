$(document).ready(function() {
    $('#getLocation').click(function() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                function(position) {
                    var latitude = position.coords.latitude;
                    var longitude = position.coords.longitude;
                    // Enviar para o backend
                    sendLocationToBackend(latitude, longitude);
                },
                function(error) {
                    console.error('Erro ao obter localização: ', error);
                }
            );
        } else {
            console.log('Geolocalização não é suportada por este navegador.');
        }
    });

    function sendLocationToBackend(latitude, longitude) {
        $.ajax({
            url: 'send-location/',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                latitude: latitude,
                longitude: longitude
            }),
            headers: {
                'X-CSRFToken': getCookie('csrftoken') // se estiver usando CSRF no Django
            },
            success: function(response) {
                if (response.status === 'success') {
                    alert('Ponto Registrado !')
                    $("#success-register-entrada").removeClass('d-none')
                    $("#register-ponto-entrada").addClass('d-none')
                    
                } else {
                    alert('Houve um erro, certifique-se de ligar o GPS.')
                    console.error('Erro:', response.message);
                }
            },
            error: function(xhr, status, error) {
                console.error('Erro ao enviar localização:', error);
            }
        });
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});


$(document).ready(function() {
    $('#getLocation-out').click(function() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                function(position) {
                    var latitude = position.coords.latitude;
                    var longitude = position.coords.longitude;
                    // Enviar para o backend
                    sendLocationToBackend(latitude, longitude);
                },
                function(error) {
                    console.error('Erro ao obter localização: ', error);
                }
            );
        } else {
            console.log('Geolocalização não é suportada por este navegador.');
        }
    });

    function sendLocationToBackend(latitude, longitude) {
        $.ajax({
            url: 'send-location-out/',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                latitude: latitude,
                longitude: longitude
            }),
            headers: {
                'X-CSRFToken': getCookie('csrftoken') // se estiver usando CSRF no Django
            },
            success: function(response) {
                if (response.status === 'success') {
                    alert('Ponto Registrado !')
                    $("#success-register").removeClass('d-none')
                    $("#register-ponto").addClass('d-none')
                    
                } else {
                    alert('Houve um erro, certifique-se de ligar o GPS.')
                    console.error('Erro:', response.message);
                }
            },
            error: function(xhr, status, error) {
                console.error('Erro ao enviar localização:', error);
            }
        });
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});