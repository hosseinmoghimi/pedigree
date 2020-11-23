let add_person_app = new Vue(
    {
        el: "#add-person-app",
        data: {
            first_name: '',
            last_name: '',
            birthdate: '',
            deathdate: '',
            add: 'اضافه کردن ',
            gender: 'مرد',

        },
        methods: {
            add_person: function () {



                var posting = $.post(url_add_person,
                    {
                        first_name: add_person_app.first_name,
                        last_name: add_person_app.last_name,
                        birthdate: add_person_app.birthdate,
                        deathdate: add_person_app.deathdate,
                        gender: add_person_app.gender,
                        csrfmiddlewaretoken: csrfmiddlewaretoken
                    }
                );

                // Put the results in a div
                posting.done(function (data) {

                    if (data.result === 'SUCCEED') {
                        add_person_app.first_name = ''
                        // add_person_app.last_name = ''
                        persons_app.persons.push(data.person)
                        person_app.secondary_person = data.person
                        // person_app.families=[]
                    }
                })


            },
        }
    }
)