import {Component, Input} from '@angular/core';
import {Domain} from "../../models/Domain";
import {DomainsService} from "../../services/DomainsService";
import {animate, query, stagger, style, transition, trigger} from "@angular/animations";

@Component({
  selector: 'app-domains',
  templateUrl: './domains.component.html',
  styleUrls: ['./domains.component.css'],
  animations: [
    trigger('domainsAnimation', [
      transition('* => *', [ // each time the binding value changes
        query(':enter', [
          style({opacity: 0}),
          stagger(220, [animate('1s', style({opacity: 1}))])
        ], {optional: true})
      ])
    ])
  ]
})
export class DomainsComponent {
  @Input() domains: Domain[] = [];

  constructor(private domainsService: DomainsService) { }

  async submit(term: any) {
    await this.domainsService.findPhishingDomainsByDomainName(term).subscribe(domains => this.domains = domains);
  }
}
