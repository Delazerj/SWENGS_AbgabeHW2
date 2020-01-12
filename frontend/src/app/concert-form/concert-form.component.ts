import {Component, OnInit} from '@angular/core';
import {FormBuilder, Validators} from '@angular/forms';
import {HttpClient} from '@angular/common/http';
import {ActivatedRoute, Router} from '@angular/router';
import {AlbumService} from '../service/album.service';
import {ArtistService} from '../service/artist.service';
import {GenreService} from '../service/genre.service';
import {ConcertService} from '../service/concert.service';

@Component({
    selector: 'app-concert-form',
    templateUrl: './concert-form.component.html',
    styleUrls: ['./concert-form.component.scss']
})
export class ConcertFormComponent implements OnInit {

    concertFormGroup;
    artistOptions;

    constructor(private fb: FormBuilder, private http: HttpClient, private route: ActivatedRoute,
                private router: Router,
                private albumService: AlbumService, private artistService: ArtistService,
                private genreService: GenreService, private concertService: ConcertService) {
    }

    ngOnInit() {
        const data = this.route.snapshot.data;

        this.concertFormGroup = this.fb.group({
            id: [null],
            name: ['', Validators.required],
            begin_date: [null],
            end_date: [null],
            artist: [[], Validators.required],
            over_18: [null]
        });


        this.artistService.retrieveArtistOptions().subscribe((result) => {
            this.artistOptions = result;
        });

        const id = this.route.snapshot.paramMap.get('id');
        if (id) {
            this.http.get('/api/concert/' + id + '/get')
                .subscribe((response) => {
                    this.concertFormGroup.patchValue(response, {emitEvent: false});
                });
        }

        if (data.student) {
            this.concertFormGroup.patchValue(data.student);
        }
    }

    createConcert() {
        const concert = this.concertFormGroup.value;
        if (concert.id) {
            this.concertService.updateConcert(concert).subscribe(() => {
                this.ngOnInit();
            });
        } else {
            this.concertService.createConcert(concert).subscribe(() => {
                this.ngOnInit();
            });
        }
    }
}
