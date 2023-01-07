import asyncio
import random
import re
import traceback
from typing import List, Optional

import aiohttp
from bs4 import BeautifulSoup
from parse_data.typing_for_parsing import DataTaskOfSubtopic
from logger_for_project import my_logger
from parse_data.format.format_data_in_tag import delete_excess_data_in_tag
from parse_data.get_data.get_answer import get_answer_task
from parse_data.get_data.get_data_of_task import get_data_of_task_for_subtopic


async def format_html_code(
    *,
    html_code: str,
    template_url: str,
    session: aiohttp.ClientSession,
    is_detailed: str
) -> DataTaskOfSubtopic:
    my_logger.info("Format html code...")
    formatted_html = delete_excess_data_in_tag(template_url=template_url, tag=html_code)
    my_logger.success("Html code formatted")

    my_logger.info("Getting data of task...")
    task_html, data_task = get_data_of_task_for_subtopic(html=formatted_html)
    my_logger.success("Getting data is finished")

    my_logger.info("Get solution for task...")
    time = 2
    while True:
        if time > 5:
            return None
        try:
            response = await get_answer_task(
                template_url=template_url,
                html_code=task_html,
                session=session,
                is_detailed=is_detailed,
            )
        except Exception as e:
            my_logger.error(traceback.format_exc())
            return None
        else:
            if not response:
                my_logger.info("Repeat request...")
                await asyncio.sleep(random.randint(0, time))
                time += 2
            else:
                break

    my_logger.success("Solution received")

    if formatted_html and response:
        solution_html, answer_text, id_task = response
        if id_task and isinstance(answer_text, str):
            data_task.id_task = int(id_task)
            data_task.solution_html = solution_html
            data_task.answer = answer_text
            return data_task
    return None


if __name__ == "__main__":
    print(
        asyncio.run(
            format_html_code(
                html_code="""<div class="prob_maindiv" id="maindiv918576" style="position:relative" width="100%"><div class="nobreak" style="margin:0; padding:0; clear:none"><div style="text-indent:0; padding-top:9px; margin-bottom:5px; font-weight:bold"><span class="prob_nums" style="">Тип 1 № <a href="/problem?id=27340">27340</a> <img class="briefcase" onclick="login_popup();" src="/img/briefcase--plus.png" style="filter: grayscale(0.8);" title="Добавить в вариант"/></span><a href="javascript:void(0)" onclick="login_popup();" style="border-bottom:none"><div style="vertical-align:middle; margin:0; margin-left:10px; display:inline-block; width:14px; height:14px; border-radius:8px; background-color:#a0a0a0; border: 1px solid #888;" title="Вы еще не решали это задание.
Нажмите, чтобы решить задание."></div></a></div><div align="justify" class="pbody" id="body918576" width="100%"><p class="left_margin"><img src="/get_file?id=109384" style="float:right;margin:10px;max-width:100%"/><p class="left_margin">В треугольнике <i>ABC</i> угол <i>C</i> равен 90°, высота <i>CH</i> равна 4, <i>BC</i>  =  8. Найдите <img alt=" косинус A." class="tex" src="https://ege.sdamgia.ru/formula/svg/01/01f4793c2ed47090b60a31cbc95e9f89.svg" style="vertical-align:-1.8pt"/></p></p></div></div><div align="justify" class="pbody" id="sol27340" style="clear:both;display:none" width="100%"><p class="left_margin"></p><b>Решение<!--rule_info-->. </b><p class="left_margin">Углы <i>A</i> и <i>HCB</i> равны как углы со взаимно перпендикулярными сторонами.<p class="left_margin"><center><p><img alt=" косинус A= косинус \angle HCB= дробь: числитель: CH, знаменатель: CB конец дроби =0,5. " class="tex" src="https://ege.sdamgia.ru/formula/svg/aa/aa493173c45e7ad86152a1d5ddcd91e7.svg" style="vertical-align:-8.4pt"><p class="left_margin"></p></img></p></center><p><span style="letter-spaceing:2px">Ответ</span>: 0,5.</p></p></p></div><div class="answer" style="display:none"><span style="letter-spacing: 2px;">Ответ: 0,5</span></div><div class="minor" style="clear:both"><!--np--><br/><p align="justify">Аналоги к заданию № <a href="/problem?id=27340">27340</a>: <span id="likes_27340_short"><a href="/problem?id=33999">33999</a> <a href="/problem?id=509414">509414</a> <a href="/problem?id=33961">33961</a> <a href="/problem?id=33963">33963</a> <a href="/problem?id=33965">33965</a> <a href="/problem?id=33967">33967</a> <a href="/problem?id=33969">33969</a> <a href="/problem?id=33971">33971</a> <a href="/problem?id=33973">33973</a> <a href="/problem?id=33975">33975</a> <a href="javascript:void(0)" onclick="document.getElementById('likes_27340_short').style.display = 'none'; document.getElementById('likes_27340_full').style.display = '';">...</a></span><span id="likes_27340_full" style="display:none"><a href="/problem?id=33999">33999</a> <a href="/problem?id=509414">509414</a> <a href="/problem?id=33961">33961</a> <a href="/problem?id=33963">33963</a> <a href="/problem?id=33965">33965</a> <a href="/problem?id=33967">33967</a> <a href="/problem?id=33969">33969</a> <a href="/problem?id=33971">33971</a> <a href="/problem?id=33973">33973</a> <a href="/problem?id=33975">33975</a> <a href="/problem?id=33977">33977</a> <a href="/problem?id=33979">33979</a> <a href="/problem?id=33981">33981</a> <a href="/problem?id=33983">33983</a> <a href="/problem?id=33985">33985</a> <a href="/problem?id=33987">33987</a> <a href="/problem?id=33989">33989</a> <a href="/problem?id=33991">33991</a> <a href="/problem?id=33993">33993</a> <a href="/problem?id=33995">33995</a> <a href="/problem?id=33997">33997</a> <a href="/problem?id=34001">34001</a> <a href="/problem?id=34003">34003</a></span> <a href="/test?likes=27340">Все</a></p><!--np--></div><!--np--><div><span style="">Кодификатор ФИПИ/Решу ЕГЭ: <a href="/search?keywords=1&amp;cb=1&amp;search=1.2.1 Синус, косинус, тангенс, котангенс произвольного угла" target="_blank">1.2.1 Синус, косинус, тангенс, котангенс произвольного угла</a>, <a href="/search?keywords=1&amp;cb=1&amp;search=5.1.1 Треугольник" target="_blank">5.1.1 Треугольник</a></span></div><!--np--></div>""",
                template_url="https://math-ege.sdamgia.ru",
            )
        )
    )
