import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {SongListComponent} from './song-list/song-list.component';
import {SongFormComponent} from './song-form/song-form.component';
import {LoginComponent} from './login/login.component';
import {AuthGuard} from './guards/auth.guard';
import {ConcertListComponent} from './concert-list/concert-list.component';
import {ConcertFormComponent} from './concert-form/concert-form.component';


const routes: Routes = [
  { path: 'song-list', component: SongListComponent, canActivate: [AuthGuard] },
  { path: 'song-form', component: SongFormComponent, canActivate: [AuthGuard] },
  { path: 'song-form/:id', component: SongFormComponent, canActivate: [AuthGuard] },
  { path: 'concert-list', component: ConcertListComponent, canActivate: [AuthGuard] },
  { path: 'concert-form', component: ConcertFormComponent, canActivate: [AuthGuard] },
  { path: 'concert-form/:id', component: ConcertFormComponent, canActivate: [AuthGuard] },
  { path: '', redirectTo: 'song-list', pathMatch: 'full' },
  { path: 'login', component: LoginComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
