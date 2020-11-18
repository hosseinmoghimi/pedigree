let person_app = new Vue(
    {
        el: "#person-app",
        data: {
            person: {},
            families:[],
            add: 'جستجو کن',
            selected_family:{}

        },
        methods: {
            select_family:function(family_id){
                console.log(family_id)
                person_app.families.forEach(family => {
                    if(family.id==family_id){
                        person_app.selected_family=family
                    }
                });
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