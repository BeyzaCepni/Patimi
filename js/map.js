var map;
        var veterinarians = [
            { name: 'Veteriner 1', district: 'İlçe 1', lat: 40.7128, lng: -74.0060 },
            { name: 'Veteriner 2', district: 'İlçe 2', lat: 40.7306, lng: -73.9352 },
            // Diğer veterinerler
        ];

        function initMap() {
            map = new google.maps.Map(document.getElementById('map'), {
                center: { lat: 40.7128, lng: -74.0060 }, // Başlangıçta haritanın merkezi (New York şehri örneği)
                zoom: 12 // Yakınlaştırma seviyesi
            });

            // Veterinerleri haritaya eklemek için döngü
            for (var i = 0; i < veterinarians.length; i++) {
                var vet = veterinarians[i];
                var marker = new google.maps.Marker({
                    position: { lat: vet.lat, lng: vet.lng },
                    map: map,
                    title: vet.name
                });
            }
        }

        function searchByDistrict() {
            var district = document.getElementById('districtInput').value;
            var filteredVeterinarians = veterinarians.filter(function (vet) {
                return vet.district.toLowerCase() === district.toLowerCase();
            });

            if (filteredVeterinarians.length > 0) {
                var bounds = new google.maps.LatLngBounds();
                for (var i = 0; i < filteredVeterinarians.length; i++) {
                    var vet = filteredVeterinarians[i];
                    var marker = new google.maps.Marker({
                        position: { lat: vet.lat, lng: vet.lng },
                        map: map,
                        title: vet.name
                    });
                    bounds.extend(marker.getPosition());
                }
                map.fitBounds(bounds);
            } else {
                alert('Bu ilçede veteriner bulunamadı.');
            }
        }