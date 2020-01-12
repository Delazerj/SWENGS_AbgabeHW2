import {Component, OnInit} from '@angular/core';
import {AlbumService} from '../service/album.service';
import {AbstractControl, FormBuilder, ValidatorFn, Validators} from '@angular/forms';
import {ActivatedRoute, Router} from '@angular/router';
import {HttpClient} from '@angular/common/http';
import {GenreService} from '../service/genre.service';
import {SongService} from '../service/song.service';
import {ArtistService} from '../service/artist.service';


@Component({
    selector: 'app-song-form',
    templateUrl: './song-form.component.html',
    styleUrls: ['./song-form.component.scss']
})
export class SongFormComponent implements OnInit {

    songFormGroup;
    albumOptions;
    artistOptions;
    display: boolean;


    constructor(private fb: FormBuilder, private http: HttpClient, private route: ActivatedRoute,
                private router: Router, private songService: SongService,
                private albumService: AlbumService, private artistService: ArtistService,
                private genreService: GenreService) {
    }


    ngOnInit() {
        this.songFormGroup = this.fb.group({
            id: [null],
            title: ['', this.noWordValidator()],
            artist: [[], Validators.required],
            genre: [null],
            album: [null],
            length: [3],
        });

        this.albumService.retrieveAlbumOptions().subscribe((result) => {
            this.albumOptions = result;
        });

        this.artistService.retrieveArtistOptions().subscribe((result) => {
            this.artistOptions = result;
        });

        const id = this.route.snapshot.paramMap.get('id');
        if (id) {
            this.http.get('/api/song/' + id + '/get')
                .subscribe((response) => {
                    this.songFormGroup.patchValue(response, {emitEvent: false});
                });
        }
    }

    createSong() {
        const song = this.songFormGroup.value;
        if (song.id) {
            this.songService.updateSong(song).subscribe(() => {
                this.ngOnInit();
            });
        } else {
            this.songService.createSong(song).subscribe(() => {
                this.ngOnInit();
            });
        }
    }

    close() {
        console.log('Close Dialog..');
    }

    // keine Sonder- oder Leerzeichen
    noWordValidator(): ValidatorFn {
        return(control: AbstractControl): {[key: string]: any} | null => {
            const forbidden = /\W/.test(control.value);
            return forbidden ? {character: {value: control.value}} : null;
        };
    }
}
