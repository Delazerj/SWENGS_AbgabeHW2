import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AlbumService {

  constructor(private http: HttpClient) { }

  retrieveAlbumOptions() {
    return this.http.get <any[]>('/api/album/options');
  }}
