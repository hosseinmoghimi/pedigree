let persons_app = new Vue(
    {
        el: "#persons-app",
        data: {
            persons: persons,
            add: 'جستجو کن',
            search_for: '',

        },
        methods: {
            search: function () {
                console.log(this.search_for)

                if (this.search_for === '')
                    this.persons = persons
                else
                    this.persons = persons.filter(person => person.full_name.indexOf(this.search_for) >= 0)
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
                        person_app.selected_family = {}

                    }
                })
            }
        }
    }
)