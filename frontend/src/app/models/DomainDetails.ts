export interface DomainDetails {
  name?: string;
  ip?: string;
  available?: boolean;
  location?: {
    continent?: string;
    country?: string;
    regionName?: string;
    city?: string;
    zip?: string;
    lat?: number;
    lon?: number;
    timezone?: string;
    currency?: string;
    isp?: string;
    org?: string;
    reverse?: string;
    mobile?: boolean;
    proxy?: boolean;
    hosting?: boolean;
    query?: string;
  };
}
