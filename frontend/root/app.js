var app = new Vue({
    el: '#app',
    data: {
        session: {
            username: 'bob'
        },
        qty_tables: 23
    },

    methods: {
        _session: function (event) {
            axios.get('http://localhost:8080/session')
                .then(function (response) {
                    console.log(response);
                })

        },


//    register: function (event) {
//                var app = this
//                axios.post('http://localhost:8080/register', {
//                    username: 'abc',
//                    password: '123'
//                  })
//                .then(function (response) {
////                    app.startingCity = response.data.city + ', ' + response.data.state
//                })
//                .catch(function (error) {
////                    app.startingCity = "Invalid Zipcode"
//                })
//              }
    }

})