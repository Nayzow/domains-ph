import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from "rxjs";
import {Domain} from "../models/Domain";
import {DomainDetails} from "../models/DomainDetails";
import { environment } from "../../environments/environment";

@Injectable({
  providedIn: 'root',
})
export class DomainsService {
  constructor(private http: HttpClient) {
  }

  findPhishingDomainsByDomainName(domain: string | null = null): Observable<Domain[]> {
    let url = environment.apiUrl + '/domains/';
    if (domain) {
      url += encodeURI(domain);
    }
    return this.http.get<Domain[]>(url);
  }

  findDataByDomainName(domain: string | null = null): Observable<DomainDetails> {
    let url = environment.apiUrl + '/domain/';
    if (domain) {
      url += encodeURI(domain);
    }
    return this.http.get<DomainDetails>(url);
  }
}
