let person_app = new Vue(
    {
        el: "#person-app",
        data: {
            person: person,
            add: 'جستجو کن',

        },
        methods: {

            delete_person: function () {
                var posting = $.post(delete_person_url,
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