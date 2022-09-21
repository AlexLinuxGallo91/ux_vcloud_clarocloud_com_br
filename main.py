from src.env_utils.env_utils import EnvUtils
from src.task_eval_times.task_eval_times import TaskEvalTimes
from src.webdriver_utils.webdriver_utils import WebDriverUtils
from src.timer_utils import var_results
from src.zabbix_utils.zabbix_utils import ZabbixSenderUtils


def main():
    # establece las principales variables las cuales se obtienen desde el archivo .env
    path_webdriver = EnvUtils.get_env_value('WEB_DRIVER_CHROME_PATH', '')
    url_portal = EnvUtils.get_env_value('URL_PORTAL_AMX')
    make_refresh_after_render_timeout = EnvUtils.get_env_value('MAKE_REFRESH_AFTER_TIMEOUT') in \
                                        ('true', 'True', 1, '1')
    debug = EnvUtils.get_env_value('DEBUG') in ('true', 'True', 1, '1')
    zabbix_host = EnvUtils.get_env_value('ZABBIX_HOST')
    monitored_hostname_zabbix = EnvUtils.get_env_value('HOSTNAME_MONITOR')
    monitored_hostname_key_zabbix = EnvUtils.get_env_value('HOST_KEY_MONITOR')

    # se establece el tiempo del timeout para la peticion http como para el ingreso por medio del webdriver
    # si este llega a no ser un int, se establece por defecto con el valor de 60
    try:
        timeout_render_portal = int(EnvUtils.get_env_value('TIMEOUT_LOAD_PAGE'))
    except ValueError:
        timeout_render_portal = 60

    # se obtiene un webdriver de navegador Chrome
    web_driver_chrome = WebDriverUtils.generate_webdriver_chrome(path_webdriver)

    # se toma el tiempo de carga en el portal web
    if make_refresh_after_render_timeout:
        TaskEvalTimes.verify_time_render_portal_with_refresh(web_driver_chrome, url_portal, timeout_render_portal)
    else:
        TaskEvalTimes.verify_time_render_portal(web_driver_chrome, url_portal, timeout_render_portal)

    # se procede a cerrar y terminar la sesion del navegador Chrome
    WebDriverUtils.close_webdriver_chrome(web_driver_chrome)

    # se toma el tiempo total de la peticion http
    TaskEvalTimes.verify_time_and_code_response_http(url_portal)

    # bandera que sirve para imprimir cada resultado como debug
    if debug:
        var_results.print_result()

    # se genera la lista de metricas
    metric_list = ZabbixSenderUtils.generate_list_metrics(monitored_hostname_zabbix, monitored_hostname_key_zabbix)

    if debug:
        for metric in metric_list:
            print(metric)

    ZabbixSenderUtils.send_list_metrics_to_zabbix_server(zabbix_host, metric_list)


if __name__ == '__main__':
    main()
