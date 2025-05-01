snapchat_rename_files() {
    fun() {
        unset new_name
        if [[ -z $1 ]] || [[ -z $2 ]]; then
            echo "Both argument should be passed..."
            return 1
        fi
        epoch_time=$1
        extention=$2
        formatted_date=$(date -d "@$epoch_time" "+%d-%m-%Y %H:%M:%S")
        milliseconds=$((epoch_time % 1000))
        new_name="Snapchat-${formatted_date}:${milliseconds}.$extention"
        n=0
        test -e "$new_name"
        while [[ $? -eq 0 ]]; do
            let "n+=1"
            echo $n
            new_name="Snapchat-${formatted_date}:${milliseconds}-$n.$extention"
            test -e "$new_name"
        done
    }
    for i in *; do
        epoch_time_=$(stat -c %Y "$i")
        extention=$(echo "$i" | cut -d. -f2)
        fun $epoch_time_ $extention
        if [[ -z $new_name ]]; then
            continue
        fi
        mv "$i" "$new_name"
    done
}
#snapchat_rename_files