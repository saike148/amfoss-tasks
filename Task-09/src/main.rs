use scraper::Selector;
use std::error::Error;
use csv::Writer;

fn main() -> Result<(), Box<dyn Error>> {
    let response = reqwest::blocking::get("https://crypto.com/price")?
        .text()?;
    let document = scraper::Html::parse_document(&response);

    let tr_selector = Selector::parse("tr").unwrap();
    let td_selector = Selector::parse("td.css-1nh9lk8").unwrap();

    let name_selector = scraper::Selector::parse("div.css-ttxvk0>p").unwrap();
    let price_selector = scraper::Selector::parse("div.css-b1ilzc > p").unwrap();
    let h24h_change_selector = scraper::Selector::parse("td.css-1b7j986 > p").unwrap();

    let names = document.select(&name_selector).map(|x| x.inner_html());
    let prices = document.select(&price_selector).map(|x| x.inner_html());
    let h24h_changes = document.select(&h24h_change_selector).map(|x| x.inner_html());
    let mut volumes = document.select(&tr_selector)
        .map(|row| row.select(&td_selector).next())
        .flatten()
        .map(|element| element.text().collect::<String>());
    let mut market_caps = document.select(&tr_selector)
        .map(|row| row.select(&td_selector).nth(1))
        .flatten()
        .map(|element| element.text().collect::<String>());

    let mut wtr = Writer::from_path("crypto.csv")?;

    wtr.write_record(&["NAME", "PRICE", "24H CHANGE", "24H VOLUME", "MARKET CAP"])?;

    for ((name, price), h24h_change) in names.zip(prices).zip(h24h_changes) {
        if let Some(volume) = volumes.next() {
            if let Some(market_cap) = market_caps.next() {
                wtr.write_record(&[name, price, h24h_change, volume, market_cap])?;
            }
        }
    }
    

    wtr.flush()?;
    Ok(())
}
