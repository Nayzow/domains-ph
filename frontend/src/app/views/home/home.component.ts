import {Component, OnInit} from '@angular/core';
import {animate, query, stagger, state, style, transition, trigger} from "@angular/animations";
import {timer} from "rxjs";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  animations: [
    trigger('textAnimation', [
      state('hidden', style({
        opacity: 0,
        transform: 'translateY(-100%)'
      })),
      state('visible', style({
        opacity: 1,
        transform: 'translateY(0)'
      })),
      transition('hidden => visible', animate('600ms ease-in'))
    ]),
    trigger('logoAnimation', [
      state('hidden', style({
        opacity: 0,
        transform: 'translateX(-100%)'
      })),
      state('visible', style({
        opacity: 1,
        transform: 'translateX(0)'
      })),
      transition('hidden => visible', animate('600ms ease-in'))
    ]),
  ]
})

export class HomeComponent implements OnInit {
  textState = 'hidden';
  logoState = 'hidden';

  showText() {
    this.textState = 'visible';
  }

  showLogo() {
    this.logoState = 'visible';
  }

  ngOnInit() {
    timer(200)
      .subscribe(() => {
        this.showText();
        this.showLogo();
      });
  }
}
