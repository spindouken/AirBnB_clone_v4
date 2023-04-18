$(document).ready(function () {
  const api = 'http://' + window.location.hostname;
  const dict = {};
  $(document).on('change', "input[type='checkbox']", function () {
    if (this.checked) {
      dict[$(this).data('id')] = $(this).data('name');
    } else {
      delete dict[$(this).data('id')];
    }
    const amenList = [];
    for (const key in dict) {
      amenList.push(dict[key]);
    }
    $('.amenities h4').text(amenList.join(', '));
  });

  $('button').click(function () {
    const amenities = Object.keys(dict);
    const data = {'amenities': amenities};
    fetch(api + ':5001/api/v1/places_search/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(response => response.json())
      .then(data => {
        $('section.places').empty();
        for (const place of data) {
          fetch(api + ':5001/api/v1/users/' + place.user_id)
            .then(response => response.json())
            .then(userData => {
              const html = `<article>
                <div class="title_box">
                    <h2>${place.name}</h2>
                    <div class="price_by_night">$${place.price_by_night}</div>
                    </div>
                    <div class="information">
                    <div class="max_guest">${place.max_guest} Guests</div>
                    <div class="number_rooms">${place.number_rooms} Bedrooms</div>
                    <div class="number_bathrooms">${place.number_bathrooms} Bathrooms</div>
                    </div>
                    <div class="user">
                    <strong>Owner: ${userData.first_name} ${userData.last_name}</strong>
                    </div>
                    <div class="description">
                    ${place.description}
                    </div>
                    </article>`;
              $('section.places').append(html);
            });
        }
      });
  });

  fetch(api + ':5001/api/v1/status/')
    .then(response => response.json())
    .then(data => {
      if (data.status === 'OK') {
        $('#api_status').addClass('available');
      } else {
        $('#api_status').removeClass('available');
      }
    });

  fetch(api + ':5001/api/v1/places_search/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({})
  })
    .then(response => response.json())
    .then(data => {
      for (const place of data) {
        fetch(api + ':5001/api/v1/users/' + place.user_id)
          .then(response => response.json())
          .then(userData => {
            const html = `<article>
              <div class="title_box">
                  <h2>${place.name}</h2>
                  <div class="price_by_night">$${place.price_by_night}</div>
                  </div>
                  <div class="information">
                  <div class="max_guest">${place.max_guest} Guests</div>
                  <div class="number_rooms">${place.number_rooms} Bedrooms</div>
                  <div class="number_bathrooms">${place.number_bathrooms} Bathrooms</div>
                  </div>
                  <div class="user">
                  <strong>Owner: ${userData.first_name} ${userData.last_name}</strong>
                  </div>
                  <div class="description">
                  ${place.description}
                  </div>
                  </article>`;
            $('section.places').append(html);
          });
      }
    });
});
