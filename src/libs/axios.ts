import axios, { AxiosRequestConfig } from 'axios'
interface IRequestData {
  method?: string,
  url: string,
  data?: unknown,
  contentType?: string,
  uploadConfig?: any,
  onUploadProgress?: (progress: ProgressEvent) => void,
  requestCanceler?: {
    enable: boolean,
    cancel?: () => void
  }
}
const instance = axios.create({
  withCredentials: false
})
interface IResponse {
  code: string,
  data: unknown,
  message?: string
}

// 解析参数
const formatParams = (execObj: IRequestData): AxiosRequestConfig => {
  const contentType = execObj.contentType ? execObj.contentType : 'json'
  const method = execObj.method ? execObj.method.toUpperCase() : 'GET'
  const {
    data, onUploadProgress, requestCanceler, uploadConfig
  } = execObj

  // headers配置
  const headers = {
    'Content-Type': `${contentType === 'json' ? 'application/json' : 'multipart/form-data'}; charset=UTF-8`,
    'Cache-Control': 'no-cache',
    Pragma: 'no-cache'
  }

  let mainparams: { [key:string]:any }
  const params = data || {}

  switch (method) {
    case 'POST':
      mainparams = {
        headers,
        method,
        data: params,
        uploadConfig
      }
      break
    case 'PUT':
      mainparams = {
        headers,
        method,
        data: params
      }
      break
    case 'PATCH':
      mainparams = {
        headers,
        method,
        data: params
      }
      break
    case 'DELETE':
      mainparams = {
        headers,
        method,
        data: params
      }
      break
    case 'GET':
      mainparams = {
        headers,
        method,
        params
      }
      break
    default:
      mainparams = {
        headers,
        method: 'GET',
        params
      }
      break
  }

  onUploadProgress && (mainparams.onUploadProgress = onUploadProgress)

  if (requestCanceler?.enable) {
    mainparams.cancelToken = new axios.CancelToken((c) => {
      requestCanceler.cancel = c
    })
  }

  return <AxiosRequestConfig>mainparams
}

const Request = (requestData: IRequestData): Promise<IResponse> => {
  const params: AxiosRequestConfig = formatParams(requestData)
  params.url = requestData.url
  const promise: Promise<IResponse> = instance(params) as unknown as Promise<IResponse>
  return promise
}

export { Request, IResponse }