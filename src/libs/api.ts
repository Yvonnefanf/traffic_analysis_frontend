import { Request, IResponse } from './axios'

export default {
  uploadPCAP(data: any): Promise<IResponse> {
    return Request({ method: 'GET', url: `/api/feedback` })
  },
  getTraffic(params:any): Promise<IResponse> {
    return Request({ method: 'GET', 
    url: `/api/getTraffic?ifFilter=${params.ifFilter}` })
  },
}

