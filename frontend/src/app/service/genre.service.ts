import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class GenreService {

  constructor() { }

  genreNames = {
    p: 'Pop',
    j: 'Jazz',
    r: 'Rock',
    h: 'Hip-Hop',
    v: 'Volksmusik'
  };
}
