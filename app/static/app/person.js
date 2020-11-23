let person_app = new Vue(
    {
        el: "#person-app",
        data: {
            confirm_delete: false,
            person: {},
            secondary_person: {},
            secondary_families : [],
            families: [],
            selected_family: {},
            first_name: '',


        },
        methods: {
            swap_person: function () {
                let sss=this.secondary_families
                this.secondary_families=this.families
                this.families=sss


                let temp1 = this.person
                this.person = this.secondary_person
                this.secondary_person = temp1
                this.select_person(this.person.id)
            },
            add_wife: function () {
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
            create_family: function () {
                var posting = $.post(url_create_family,
                    {
                        father_id: person_app.person.id,
                        mother_id: person_app.secondary_person.id,
                        csrfmiddlewaretoken: csrfmiddlewaretoken
                    }
                );

                // Put the results in a div
                posting.done(function (data) {

                    if (data.result === 'SUCCEED') {
                        person_app.families.push(data.family)
                      
                    }
                })

            },

            add_child_to_family: function (child_id, family) {


                var posting = $.post(url_add_child,
                    {
                        child_id: child_id,
                        first_name: ' - ',
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
            select_secondary_person: function (person_id) {
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
                        person_app.secondary_person = data.person

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
                        person_app.person = person_app.secondary_person
                        person_app.confirm_delete=false
                    }
                })
            },

        }
    }
)
