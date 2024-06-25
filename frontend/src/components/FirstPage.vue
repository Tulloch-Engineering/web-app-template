<template>
  <div>
    <div>First Page</div>
  </div>
</template>

<script>

export default {
  name: 'FirstPage',
  setup() {
    const map = ref(null);
    const data = ref(null);

    const initializeMap = (latitude, longitude) => {
      map.value = L.map('map').setView([latitude, longitude], 13);

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
      }).addTo(map.value);

      L.marker([latitude, longitude]).addTo(map.value)
        .bindPopup('You are here!')
        .openPopup();
    };

    const successCallback = (position) => {
      const { latitude, longitude } = position.coords;
      data.value = position.coords;
      initializeMap(latitude, longitude);
    };

    const errorCallback = (error) => {
      console.error(error);
    };

    onMounted(() => {
      navigator.geolocation.getCurrentPosition(successCallback, errorCallback, {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0
      });
    });

    return { data };
  }
};
</script>

<style scoped>
#map {
  height: 100%;
}
</style>
