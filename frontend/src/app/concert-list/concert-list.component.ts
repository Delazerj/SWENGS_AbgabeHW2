import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {ConcertService} from '../service/concert.service';


@Component({
  selector: 'app-concert-list',
  templateUrl: './concert-list.component.html',
  styleUrls: ['./concert-list.component.scss']
})
export class ConcertListComponent implements OnInit {
  concerts: any[];
  displayedColumns = ['name', 'begin_date', 'end_date', 'artist_name', 'id'];

  constructor(private http: HttpClient, public concertService: ConcertService) { }

  ngOnInit() {
    this.concertService.getConcerts()
        .subscribe((response: any[]) => {
          this.concerts = response;
        });
  }

  deleteConcert(concert) {
    this.concertService.deleteConcert(concert)
        .subscribe(() => {
          this.ngOnInit();
        });
  }

}
