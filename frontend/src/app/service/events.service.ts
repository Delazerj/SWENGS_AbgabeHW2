import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})
export class EventsService {
    constructor(private http: HttpClient) {
    }

    getEvents() {
        return this.http.get('/api/events/list');
    }

    createEvent(event) {
        return this.http.post('/api/events/create', event);
    }

    updateEvent(event) {
        return this.http.put('/api/events/' + event.id + '/update', event);
    }

    deleteEvent(event) {
        return this.http.delete('/api/events/' + event.id + '/delete', event);
    }
}
