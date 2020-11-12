let persons_app=new Vue(
    {
        el:"#persons-app",
        data:{
            persons:persons,
            add:'جستجو کن',

        },
        methods:{
            select_person:function(person_id){
                var posting = $.post(get_person_url,
                    {
                        person_id: person_id,                        
                        csrfmiddlewaretoken: csrfmiddlewaretoken
                    }
                );

                // Put the results in a div
                posting.done(function (data) {

                    if (data.result === 'SUCCEED') {
                        person=data.person
                        person_app.person=data.person
                    console.log(person)

                    }
                })
            }
        }
    }
)