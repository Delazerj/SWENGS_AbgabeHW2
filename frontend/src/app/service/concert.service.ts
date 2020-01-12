import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ConcertService {

  constructor(private http: HttpClient) {
  }

  getConcerts() {
    return this.http.get('/api/concert/list');
  }

  createConcert(concert) {
    return this.http.post('/api/concert/create', concert);
  }

  updateConcert(concert) {
    return this.http.put('/api/concert/' + concert.id + '/update', concert);
  }

  deleteConcert(concert) {
    return this.http.delete('/api/concert/' + concert.id + '/delete', concert);
  }
}
