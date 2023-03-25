import {Component, OnInit} from '@angular/core';
import {DomainsService} from "../../services/DomainsService";
import {DomainDetails} from "../../models/DomainDetails";
import * as URL from 'url';

@Component({
  selector: 'app-domain',
  templateUrl: './domain.component.html',
  styleUrls: ['./domain.component.css']
})
export class DomainComponent implements OnInit {
  path: string | null = null;
  domainName: string | null = null;
  domain: DomainDetails | null = null;
  latitude: number | undefined;
  longitude: number | undefined;

  constructor(private domainsService: DomainsService) {
    this.path = URL.parse(window.location.href).pathname;
    // @ts-ignore
    this.domainName = this.path.split('/').pop();
  }

  setLocation(latitude: number | undefined, longitude: number | undefined) {
    this.latitude = latitude;
    this.longitude = longitude;
  }

  ngOnInit() {
    this.domainsService.findDataByDomainName(this.domainName).subscribe(domain => {
      this.domain = domain;
     // this.domain ? this.setLocation(this.domain.lat, this.domain.lon) : this.setLocation(0, 0);
    });
  }
}
