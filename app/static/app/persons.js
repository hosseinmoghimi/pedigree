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
                if (this.search_for.length == 3) {

                    var posting = $.post(url_search_person,
                        {
                            search_for: persons_app.search_for,
                            csrfmiddlewaretoken: csrfmiddlewaretoken
                        }
                    );

                    // Put the results in a div
                    posting.done(function (data) {

                        if (data.result === 'SUCCEED') {
                            persons_app.persons = data.persons
                        }
                    })


                }
                // if (this.search_for.length > 3) {
                else {
                    persons_app.start_search(this.search_for)
                }
            },
            start_search: function (search_for) {

                persons_app.persons = persons_app.persons.filter(person => person.full_name.indexOf(this.search_for) >= 0)
                // perrsons = persons_app.persons.filter(person => person.full_name.indexOf(this.search_for) >= 0)
                // perrsons = persons_app.persons.filter(person => person.full_name.indexOf(this.search_for) >= 0)
                // persons_app.persons = persons
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