use std::env;
use std::fs;
use std::path::PathBuf;

#[derive(Clone)]
struct Config {
    target_version: String,
    payload_path: PathBuf,
    active_slot: String,
    once: bool,
}

fn parse_args() -> Config {
    let mut target_version = String::from("1.0.0");
    let mut payload_path = PathBuf::from("update.bundle");
    let mut active_slot = String::from("A");
    let mut once = false;

    let mut args = env::args().skip(1);
    while let Some(argument) = args.next() {
        match argument.as_str() {
            "--target-version" => {
                if let Some(value) = args.next() {
                    target_version = value;
                }
            }
            "--payload-path" => {
                if let Some(value) = args.next() {
                    payload_path = PathBuf::from(value);
                }
            }
            "--active-slot" => {
                if let Some(value) = args.next() {
                    active_slot = value;
                }
            }
            "--once" => {
                once = true;
            }
            _ => {}
        }
    }

    Config {
        target_version,
        payload_path,
        active_slot,
        once,
    }
}

fn inactive_slot(active_slot: &str) -> &str {
    if active_slot.eq_ignore_ascii_case("A") {
        "B"
    } else {
        "A"
    }
}

fn payload_size(path: &PathBuf) -> u64 {
    fs::metadata(path).map(|metadata| metadata.len()).unwrap_or(0)
}

fn main() {
    let config = parse_args();
    let inactive_slot = inactive_slot(&config.active_slot);
    let bundle_size = payload_size(&config.payload_path);

    println!(
        "{{\"component\":\"ota_agent\",\"target_version\":\"{}\",\"payload_path\":\"{}\",\"active_slot\":\"{}\",\"inactive_slot\":\"{}\",\"bundle_size\":{},\"verify_only\":{}}}",
        config.target_version,
        config.payload_path.display(),
        config.active_slot,
        inactive_slot,
        bundle_size,
        if config.once { "true" } else { "false" }
    );
}
