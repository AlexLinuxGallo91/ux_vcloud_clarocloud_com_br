from pyzabbix import ZabbixSender, ZabbixMetric
from src.timer_utils import var_results
import socket


class ZabbixSenderUtils:

    @staticmethod
    def generate_list_metrics(hostname: str, host_key: str):
        metric_list = [
            ZabbixMetric(host=hostname, key='{}.{}'.format(host_key, var_results.HOST_KEY_TIME_TOTAL_RENDER_PORTAL),
                         value=var_results.TIME_TOTAL_RENDER_PORTAL),
            ZabbixMetric(host=hostname,
                         key='{}.{}'.format(host_key, var_results.HOST_KEY_RESULT_PORTAL_RENDERED_IS_CORRECT),
                         value=var_results.RESULT_PORTAL_RENDERED_IS_CORRECT),
            ZabbixMetric(host=hostname, key='{}.{}'.format(host_key, var_results.HOST_KEY_HTTP_TIME_TOTAL_RESPONSE),
                         value=var_results.HTTP_TIME_TOTAL_RESPONSE),
            ZabbixMetric(host=hostname, key='{}.{}'.format(host_key, var_results.HOST_KEY_HTTP_STATUS_CODE),
                         value=var_results.HTTP_STATUS_CODE)]

        return metric_list

    @staticmethod
    def send_list_metrics_to_zabbix_server(zabbix_server_ip: str, metric_list: list):
        metrics_sended_correctly = True
        zabbix_sender = ZabbixSender(zabbix_server=zabbix_server_ip)

        try:
            resp = zabbix_sender.send(metric_list)
            print(resp)
        except ConnectionRefusedError:
            metrics_sended_correctly = False
        except TimeoutError:
            metrics_sended_correctly = False
        except socket.error:
            metrics_sended_correctly = False

        print('se enviaron correctamente las metricas?: {}'.format(metrics_sended_correctly))

        return metrics_sended_correctly
