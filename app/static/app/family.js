let family_app = new Vue(
    {
        el: "#family-app",
        data: {
            family:{},

        },
        methods: {
            select_family:function(family_id){
                var posting = $.post(url_select_family,
                    {
                        family_id: family_id,
                        csrfmiddlewaretoken: csrfmiddlewaretoken
                    }
                );

                // Put the results in a div
                posting.done(function (data) {

                    if (data.result === 'SUCCEED') {
                        family_app.family=data.family
                    }
                })

            },
            select_person: function (person_id) {
                var posting = $.post(url_get_person,
                    {
                        person_id: person_id,
                        csrfmiddlewaretoken: csrfmiddlewaretoken
                    }
                );

                // Put the results in a div
                posting.done(function (data) {

                    if (data.result === 'SUCCEED') {
                        person = data.person
                        person_app.person = data.person
                        person_app.families = data.families

                    }
                })
            },
            delete_person: function () {
                var posting = $.post(url_delete_person,
                    {
                        person_id: person_app.person.id,
                        csrfmiddlewaretoken: csrfmiddlewaretoken
                    }
                );

                // Put the results in a div
                posting.done(function (data) {
                    console.log(data)
                    if (data.result === 'SUCCEED') {
                        persons_app.persons = data.persons
                    }
                })
            },

        }
    }
)