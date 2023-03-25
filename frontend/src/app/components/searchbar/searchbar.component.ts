import {Component, EventEmitter, Output} from '@angular/core';

@Component({
  selector: 'app-searchbar',
  templateUrl: './searchbar.component.html',
  styleUrls: ['./searchbar.component.css']
})
export class SearchbarComponent {
  term: string | undefined;
  @Output() submit = new EventEmitter<string>();
}
