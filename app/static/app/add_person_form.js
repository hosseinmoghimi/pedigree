let add_person_app = new Vue(
    {
        el: "#add-person-app",
        data: {
            first_name: '',
            last_name: '',
            birthdate: '',
            deathdate: '',
            add: 'اضافه کن',

        },
        methods: {
            add_person: function () {



                var posting = $.post(add_person_url,
                    {
                        first_name: add_person_app.first_name,
                        last_name: add_person_app.last_name,
                        birthdate: add_person_app.birthdate,
                        deathdate: add_person_app.deathdate,
                        csrfmiddlewaretoken: csrfmiddlewaretoken
                    }
                );

                // Put the results in a div
                posting.done(function (data) {

                    if (data.result === 'SUCCEED') {
                        add_person_app.first_name = ''
                        add_person_app.last_name = ''
                        persons_app.persons.push(data.person)
                        person_app.person=data.person
                    }
                })


            },
        }
    }
)