
const config = {
    style: "mapbox://styles/mapbox/dark-v10",
    accessToken: "pk.eyJ1IjoidHJldm9yc3BlY2h0IiwiYSI6ImNrYzJoM2t4ODAxNDAycnF0cHo5eHoybDcifQ.-Pw1y6ZbWuUMooRWmJAK1Q",
    CSV: "https://docs.google.com/spreadsheets/d/1TLU9QKCgdmhtlme6szcqdyc7Y70-qJJsATEHwlQPv88/gviz/tq?tqx=out:csv&sheet=Sheet1",
    center: [-76.610759, 39.2908816], //Lng, Lat
    zoom: 11, //Default zoom
    title: "Baltimore Black-owned Restaurants",
    description: "You can search by cuisine to sort the list below by cuisine type.",
    sideBarInfo: ["Name", "Address", "Website", "Phone"],
    popupInfo: ["Name", "Website"],
    filters: [
        {
            type: "dropdown",
            title: "Cuisines",
            columnHeader: "Cuisine",
            listItems: [
              'African/Caribbean',
              'American',
              'Asian',
              'Breakfast Specialty',
              'Seafood',
              'Soul/Creole',
              'Vegan/Healthy',
              'Dessert',
              'Coffee/Tea'
            ]
        }
      /*  {
            type: "checkbox",
            title: "Title of filter: ",
            columnHeader: "Column Name",
            listItems: ["filter one", "filter two", "filter three"]
        },
        {
            type: "dropdown",
            title: "Title of filter: ",
            columnHeader: "Column Name",
            listItems: [
                'filter one',
                'filter two',
                'filter three',
                'filter four',
                'filter five',
                'filter six',
                'filter seven'
            ]
        }
        */
    ]

};
