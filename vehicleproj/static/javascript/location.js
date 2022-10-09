const options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 10
  };
  
  function success(pos) {
    const crd = pos.coords;
    document.getElementById('lat').value=crd.latitude;
    document.getElementById('lon').value=crd.longitude;
    
 }
  
  function error(err) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
    alert("allow location");
  }
  
navigator.geolocation.getCurrentPosition(success, error, options);
