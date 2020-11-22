let person_app = new Vue(
    {
        el: "#person-app",
        data: {
            person: {},
            families: [],
            selected_family: {},
            first_name: '',


        },
        methods: {
            add_wife:function(){
                var posting = $.post(url_add_wife,
                    {
                        first_name: person_app.first_name,
                        family_id: family.id,
                        csrfmiddlewaretoken: csrfmiddlewaretoken
                    }
                );

                // Put the results in a div
                posting.done(function (data) {

                    if (data.result === 'SUCCEED') {
                        person_app.first_name = ''
                        person_app.families.forEach(family => {
                            if (family.id == data.family.id) {
                                family.childs = data.family.childs
                            }

                        });
                    }
                })

            },
            add_child: function (family) {


                var posting = $.post(url_add_child,
                    {
                        first_name: person_app.first_name,
                        family_id: family.id,
                        csrfmiddlewaretoken: csrfmiddlewaretoken
                    }
                );

                // Put the results in a div
                posting.done(function (data) {

                    if (data.result === 'SUCCEED') {
                        person_app.first_name = ''
                        person_app.families.forEach(family => {
                            if (family.id == data.family.id) {
                                family.childs = data.family.childs
                            }

                        });
                    }
                })


            },
            show_family: function (family) {
                let father_name = family.father ? family.father.full_name : ''
                let mother_name = family.mother ? family.mother.full_name : ''
                let template = `
                <div class="text-light">${father_name}</div>
                <div class="text-secondary">${mother_name}</divlight>
                `
                return template
            },
            select_family: function (family) {

                person_app.selected_family = family
                // this.full_name=family.father?family.father.last_name:''

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
                        person_app.selected_family = data.families[0]

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
