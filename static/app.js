function printdata(data){
    console.log(data);
}
function addForm(){
    var val = 0;
    var element = (
        `<div>
            <label for="event-title">Event Title:</label>
            <input type="text" class="ininfo" id="event-title${val}" name="event-title" value="">

            <label for="start-date">Start Date:</label>
            <input type="date" class="ininfo" id="start-date${val}" name="start-date" value="">

            <label for="start-time">Start Time:</label>
            <input type="time" class="ininfo" id="start-time${val}" name="start-time" value="">

            <label for="end-date">End Date:</label>
            <input type="date" class="ininfo" id="end-date${val}" name="end-date" value="">

            <label for="end-time">End Time:</label>
            <input type="time" class="ininfo" id="end-time${val}" name="end-time" value="">

            <label for="description">Notes/Description:</label>
            <textarea id="description${val}" name="description" value=""></textarea>
        </div>`
    )
    document.getElementById('container').innerHTML += element;
    val++;
}

function buildConfig(data){
    var dict = [{'kind': 'calendar#event', 
    'etag': '"3364101439047000"', 
    'id': '6o35s3fp1o0342f8v7bn40f3aj', 
    'status': 'confirmed', 
    'htmlLink': 'https://www.google.com/calendar/event?eid=Nm8zNXMzZnAxbzAzNDJmOHY3Ym40MGYzYWogdG9jOGJuZ3JkdG5qMnJybGZuaGNiM3Y3bDRAZw', 
    'created': '2023-04-19T17:59:08.000Z', 
    'updated': '2023-04-22T14:11:00.318Z', 
    'summary': 'Test #1', 
    'creator': {'email': 'luisgallegos0316@gmail.com'}, 
    'organizer': {'email': 'toc8bngrdtnj2rrlfnhcb3v7l4@group.calendar.google.com', 'displayName': 'test', 'self': True}, 
    'start': {'date': '2023-04-23'}, 
    'end': {'date': '2023-04-24'}, 
    'transparency': 'transparent', 
    'iCalUID': '6o35s3fp1o0342f8v7bn40f3aj@google.com', 
    'sequence': 1, 
    'reminders': {'useDefault': False},
     'eventType': 'default'}, 
     {'kind': 'calendar#event', 
     'etag': '"3364101457188000"', 
     'id': '4s4im9subfu3b6ksoppv4b93lp', 
     'status': 'confirmed', 
     'htmlLink': 'https://www.google.com/calendar/event?eid=NHM0aW05c3ViZnUzYjZrc29wcHY0YjkzbHAgdG9jOGJuZ3JkdG5qMnJybGZuaGNiM3Y3bDRAZw', 
     'created': '2023-04-19T17:59:14.000Z', 
     'updated': '2023-04-22T14:11:02.183Z', 
     'summary': 'Test 2', 
     'creator': {'email': 'luisgallegos0316@gmail.com'}, 
     'organizer': {'email': 'toc8bngrdtnj2rrlfnhcb3v7l4@group.calendar.google.com', 'displayName': 'test', 'self': True}, 
     'start': {'date': '2023-04-24'}, 
     'end': {'date': '2023-04-25'},
      'transparency': 'transparent', 
      'iCalUID': '4s4im9subfu3b6ksoppv4b93lp@google.com', 
      'sequence': 1, 'reminders': {'useDefault': False}, 
      'eventType': 'default'},
       {'kind': 'calendar#event', 
       'etag': '"3364101467681000"', 
       'id': '4e1k365ik495eg1rmtuj47j0c3', 
       'status': 'confirmed', 
       'htmlLink': 'https://www.google.com/calendar/event?eid=NGUxazM2NWlrNDk1ZWcxcm10dWo0N2owYzMgdG9jOGJuZ3JkdG5qMnJybGZuaGNiM3Y3bDRAZw', 
       'created': '2023-04-19T17:59:19.000Z', 
       'updated': '2023-04-22T14:11:04.236Z', 
       'summary': 'Test 3', 
       'creator': {'email': 'luisgallegos0316@gmail.com'}, 
       'organizer': {'email': 'toc8bngrdtnj2rrlfnhcb3v7l4@group.calendar.google.com', 'displayName': 'test', 'self': True}, 
       'start': {'date': '2023-04-25'}, 
       'end': {'date': '2023-04-26'}, 
       'transparency': 'transparent', 
       'iCalUID': '4e1k365ik495eg1rmtuj47j0c3@google.com', 
       'sequence': 1, 
       'reminders': {'useDefault': False}, 
       'eventType': 'default'}]
}