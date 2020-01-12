import {Component, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {GenreService} from '../service/genre.service';
import {SongService} from '../service/song.service';

@Component({
  selector: 'app-song-list',
  templateUrl: './song-list.component.html',
  styleUrls: ['./song-list.component.scss']
})
export class SongListComponent implements OnInit {
  songs: any[];
  displayedColumns = ['title', 'artist_name', 'album_name', 'genre', 'id'];

  constructor(private http: HttpClient, public genreService: GenreService, public songService: SongService) {
  }

  ngOnInit() {
    this.songService.getSongs()
        .subscribe((response: any[]) => {
          this.songs = response;
        });
  }

  deleteSong(song) {
    this.songService.deleteSong(song)
        .subscribe(() => {
          this.ngOnInit();
        });
  }
}
